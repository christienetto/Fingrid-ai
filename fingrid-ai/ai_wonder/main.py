import os
from crewai import Agent, Task, Crew, Process
from langchain_groq import ChatGroq
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

os.environ["GROQ_API_KEY"] = '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'

openai_llm = ChatGroq(api_key=os.environ.get("GROQ_API_KEY"), model="groq/llama-3.1-70b-versatile")

# Define the AI agents with updated goals
postSummarizerAI = Agent(
    role='Post Analyzer',
    goal="Analyze posts to provide comprehensive summaries and categorize the post type",
    backstory="""You are an expert at analyzing technical posts in an energy infrastructure platform context. 
    You can identify key issues, technical details, and categorize posts into relevant business categories.""",
    description="""Analyzes posts to provide:
    1. Post categories (Technical Issue, Feature Request, Billing Query, Infrastructure Update, etc.)
    2. Detailed summary of content
    3. Technical and business context""",
    verbose=True,
    allow_delegation=False,
    llm=openai_llm,
)

techChatbotAI = Agent(
    role='Technical Support Chatbot',
    goal="Provide helpful responses to user questions about the analyzed post",
    backstory="You are a knowledgeable technical support assistant who can answer questions about the post's content and provide relevant guidance",
    description="Responds to user queries about the post with accurate and helpful information",
    verbose=False,
    allow_delegation=False,
    llm=openai_llm,
)

class PostAnalysisInterface:
    def __init__(self, master):
        self.master = master
        master.title("Post Analysis System")
        master.geometry("1000x800")
        master.configure(bg='#f0f0f0')
        
        # Configure fonts
        self.title_font = tkfont.Font(family="Helvetica", size=14, weight="bold")
        self.label_font = tkfont.Font(family="Helvetica", size=11)
        self.text_font = tkfont.Font(family="Georgia", size=12)
        self.category_font = tkfont.Font(family="Helvetica", size=10, weight="bold")
        
        self.create_widgets()
        self.current_post = ""
        self.current_summary = ""
        self.current_categories = []

    def create_widgets(self):
        # Main container
        main_container = ttk.PanedWindow(self.master, orient=tk.HORIZONTAL)
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Left panel for post input and summary
        left_panel = ttk.Frame(main_container)
        main_container.add(left_panel, weight=1)

        # Right panel for chat
        right_panel = ttk.Frame(main_container)
        main_container.add(right_panel, weight=1)

        # Left panel contents
        ttk.Label(left_panel, text="Paste Post Content:", font=self.label_font).pack(anchor=tk.W, pady=(0, 5))
        self.post_input = tk.Text(left_panel, height=15, wrap=tk.WORD, font=self.text_font)
        self.post_input.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        ttk.Button(left_panel, text="Analyze Post", command=self.analyze_post).pack(pady=(0, 10))

        # Categories section
        ttk.Label(left_panel, text="Post Categories:", font=self.label_font).pack(anchor=tk.W, pady=(0, 5))
        self.categories_text = tk.Text(left_panel, height=2, wrap=tk.WORD, font=self.category_font, state="disabled")
        self.categories_text.pack(fill=tk.X, pady=(0, 10))

        # Summary section
        ttk.Label(left_panel, text="Post Summary:", font=self.label_font).pack(anchor=tk.W, pady=(0, 5))
        self.summary_text = tk.Text(left_panel, height=10, wrap=tk.WORD, font=self.text_font, state="disabled")
        self.summary_text.pack(fill=tk.BOTH, expand=True)

        # Right panel contents
        ttk.Label(right_panel, text="Chat with AI about the Post:", font=self.label_font).pack(anchor=tk.W, pady=(0, 5))
        
        self.chat_history = tk.Text(right_panel, height=20, wrap=tk.WORD, font=self.text_font, state="disabled")
        self.chat_history.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        chat_input_frame = ttk.Frame(right_panel)
        chat_input_frame.pack(fill=tk.X, pady=(0, 10))

        self.chat_input = tk.Text(chat_input_frame, height=3, wrap=tk.WORD, font=self.text_font)
        self.chat_input.pack(side=tk.LEFT, fill=tk.X, expand=True)

        ttk.Button(chat_input_frame, text="Send", command=self.send_message).pack(side=tk.RIGHT, padx=(10, 0))

    def analyze_post(self):
        post_content = self.post_input.get("1.0", tk.END).strip()
        if post_content:
            self.current_post = post_content
            
            # Create a specific task for analysis and categorization
            analyze_task = Task(
                description=f"""Analyze this post and provide:
                1. CATEGORIES: Identify 1-3 most relevant categories from the following options (or suggest better ones if needed):
                   - Technical Issue/Bug
                   - Feature Request
                   - Billing Query
                   - Infrastructure Update
                   - API Integration
                   - Performance Issue
                   - Security Concern
                   - Contractual Change
                   - Documentation Request
                   - Service Degradation
                
                2. SUMMARY: Create a detailed summary that includes:
                   - Main issue or topic being discussed
                   - Company name (if mentioned)
                   - Current infrastructure and technologies (if mentioned)
                   - Any other relevant technical details
                
                Format the response with clear CATEGORIES: and SUMMARY: sections.
                
                Post content: {post_content}""",
                agent=postSummarizerAI,
                expected_output="Categorized and structured summary of the post"
            )
            
            # Create a crew for analysis
            analysis_crew = Crew(
                agents=[postSummarizerAI],
                tasks=[analyze_task]
            )
            
            result = analysis_crew.kickoff()
            
            # Split the result into categories and summary
            result_str = str(result)
            categories_part = ""
            summary_part = ""
            
            if "CATEGORIES:" in result_str and "SUMMARY:" in result_str:
                parts = result_str.split("SUMMARY:")
                categories_part = parts[0].replace("CATEGORIES:", "").strip()
                summary_part = parts[1].strip()
            else:
                summary_part = result_str
            
            self.current_summary = summary_part
            self.update_categories(categories_part)
            self.update_summary(summary_part)
            self.update_chat_history("System: Post analyzed. You can now ask questions about it.\n")
        else:
            self.update_summary("Please paste a post to analyze.")

    def update_categories(self, text):
        self.categories_text.configure(state="normal")
        self.categories_text.delete("1.0", tk.END)
        self.categories_text.insert("1.0", text)
        self.categories_text.configure(state="disabled")

    def send_message(self):
        message = self.chat_input.get("1.0", tk.END).strip()
        if message and self.current_post:
            self.update_chat_history(f"You: {message}\n")
            
            # Create a specific task for chat response
            chat_task = Task(
                description=f"""Based on this context, provide a helpful response to the user's question.
                Original Post: {self.current_post}
                Post Summary: {self.current_summary}
                User Question: {message}""",
                agent=techChatbotAI,
                expected_output="Detailed and relevant response to the user's question about the post"
            )
            
            # Create a crew for chat response
            chat_crew = Crew(
                agents=[techChatbotAI],
                tasks=[chat_task]
            )
            
            response = chat_crew.kickoff()
            self.update_chat_history(f"AI: {response}\n")
            self.chat_input.delete("1.0", tk.END)
        else:
            if not self.current_post:
                self.update_chat_history("System: Please analyze a post first before asking questions.\n")
            else:
                self.update_chat_history("System: Please enter a question.\n")

    def update_summary(self, text):
        self.summary_text.configure(state="normal")
        self.summary_text.delete("1.0", tk.END)
        self.summary_text.insert("1.0", text)
        self.summary_text.configure(state="disabled")

    def update_chat_history(self, text):
        self.chat_history.configure(state="normal")
        self.chat_history.insert(tk.END, text)
        self.chat_history.configure(state="disabled")
        self.chat_history.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = PostAnalysisInterface(root)
    root.mainloop()