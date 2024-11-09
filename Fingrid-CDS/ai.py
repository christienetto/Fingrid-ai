import os
from crewai import Agent, Task, Crew, Process
from langchain_groq import ChatGroq

class PostAnalysisSystem:
    def __init__(self):
        # Set API key
        os.environ["GROQ_API_KEY"] = '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'
        self.api_key = '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'
        
        # Initialize LLM
        self.openai_llm = ChatGroq(api_key=self.api_key, model="groq/llama-3.1-70b-versatile")
        
        # Initialize agents
        self.post_summarizer_ai = Agent(
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
            llm=self.openai_llm,
        )

        self.tech_chatbot_ai = Agent(
            role='Technical Support Chatbot',
            goal="Provide helpful responses to user questions about the analyzed post",
            backstory="You are a knowledgeable technical support assistant who can answer questions about the post's content and provide relevant guidance",
            description="Responds to user queries about the post with accurate and helpful information",
            verbose=False,
            allow_delegation=False,
            llm=self.openai_llm,
        )
        
        # Store current post information
        self.current_post = ""
        self.current_summary = ""
        self.current_categories = []

    def analyze_post(self, post_content):
        """
        Analyze a post and return its categories and summary.
        
        Args:
            post_content (str): The content of the post to analyze
            
        Returns:
            dict: A dictionary containing categories and summary
        """
        if not post_content:
            return {"error": "Post content cannot be empty"}
            
        self.current_post = post_content
        
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
            agent=self.post_summarizer_ai,
            expected_output="Categorized and structured summary of the post"
        )
        
        analysis_crew = Crew(
            agents=[self.post_summarizer_ai],
            tasks=[analyze_task]
        )
        
        result = analysis_crew.kickoff()
        result_str = str(result)
        
        # Parse the result
        categories = ""
        summary = ""
        
        if "CATEGORIES:" in result_str and "SUMMARY:" in result_str:
            parts = result_str.split("SUMMARY:")
            categories = parts[0].replace("CATEGORIES:", "").strip()
            summary = parts[1].strip()
        else:
            summary = result_str
            
        self.current_summary = summary
        self.current_categories = categories
        
        return {
            "categories": categories,
            "summary": summary
        }

    def chat_with_ai(self, user_message):
        """
        Send a message to the AI about the analyzed post and get a response.
        
        Args:
            user_message (str): The user's question about the post
            
        Returns:
            str: The AI's response
        """
        if not self.current_post:
            return "Error: Please analyze a post first before asking questions."
            
        if not user_message:
            return "Error: Please provide a question."
            
        chat_task = Task(
            description=f"""Based on this context, provide a helpful response to the user's question.
            Original Post: {self.current_post}
            Post Summary: {self.current_summary}
            User Question: {user_message}""",
            agent=self.tech_chatbot_ai,
            expected_output="Detailed and relevant response to the user's question about the post"
        )
        
        chat_crew = Crew(
            agents=[self.tech_chatbot_ai],
            tasks=[chat_task]
        )
        
        response = chat_crew.kickoff()
        return str(response)

    def get_current_context(self):
        """
        Get the current post context.
        
        Returns:
            dict: The current post, summary, and categories
        """
        return {
            "post": self.current_post,
            "summary": self.current_summary,
            "categories": self.current_categories
        }