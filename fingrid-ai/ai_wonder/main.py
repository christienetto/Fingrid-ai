import os
from crewai import Agent, Task, Crew, Process
from langchain_groq import ChatGroq
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

os.environ["GROQ_API_KEY"] = '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'

openai_llm = ChatGroq(api_key=os.environ.get("GROQ_API_KEY"), model="groq/llama-3.1-70b-versatile")

poemCreatorAI = Agent(
    role='Poetic Verse Creator',
    goal="Create first two lines of a four-line poem based on user input, focusing on imagery and emotion",
    backstory="You are a skilled poet who can transform any topic into evocative verse, specializing in creating opening lines that set the tone and theme",
    description="Creates the first two lines of poems that capture the essence of any given topic",
    verbose=True,
    allow_delegation=False,
    llm=openai_llm,
)

poemFinisherAI = Agent(
    role='Poem Concluder',
    goal="Complete the four-line poem by adding two final lines that complement the opening verses",
    backstory="You are a master of poetic closure, crafting perfect endings that bring depth and resolution to poems",
    description="Creates the final two lines of poems, ensuring they connect thematically with the opening lines",
    verbose=False,
    allow_delegation=False,
    llm=openai_llm,
)

opening_lines_task = Task(
    description="Create the first two lines of a poem based on the user's input. Focus on creating vivid imagery and establishing the poem's theme.",
    agent=poemCreatorAI,
    expected_output="First two lines of a poem about {input}",
)

closing_lines_task = Task(
    description="Create the final two lines of the poem that complement and conclude the opening lines",
    agent=poemFinisherAI,
    expected_output="Complete four-line poem about {input}",
)

crew = Crew(
    agents=[poemCreatorAI, poemFinisherAI], 
    tasks=[opening_lines_task, closing_lines_task]
)

def functionality(question):    
    while(True):
        if question == "q":
            return "Thank you for sharing poetic moments with me! ♥"
        result = crew.kickoff(inputs={"input": question})
        if "agent has" in str(result).lower():
            return "The muse is silent today, please try again..."
        return result

class SimplifiedInterface:
    def __init__(self, master):
        self.master = master
        master.title("Poetry Generation Interface")
        master.geometry("800x600")
        master.configure(bg='#f0f0f0')

        self.is_recording = False
        self.record_text_index = 0
        
        # Configure fonts
        self.title_font = tkfont.Font(family="Helvetica", size=14, weight="bold")
        self.label_font = tkfont.Font(family="Helvetica", size=11)
        self.text_font = tkfont.Font(family="Georgia", size=12)
        
        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = ttk.Label(
            self.master, 
            text="AI Poetry Generator", 
            font=self.title_font
        )
        title_label.pack(pady=(20, 10))

        # Input Frame
        input_frame = ttk.Frame(self.master, padding="10")
        input_frame.pack(fill=tk.X, pady=(0, 10))

        input_label = ttk.Label(
            input_frame, 
            text="Enter your poetry theme:", 
            font=self.label_font
        )
        input_label.pack(anchor=tk.W)

        self.input_entry = tk.Text(
            input_frame, 
            wrap=tk.WORD, 
            height=3, 
            font=self.text_font
        )
        self.input_entry.pack(fill=tk.X, expand=True)

        # Button Frame
        button_frame = ttk.Frame(input_frame)
        button_frame.pack(pady=(10, 0))

        submit_button = ttk.Button(
            button_frame, 
            text="Generate Poem", 
            command=self.on_submit
        )
        submit_button.pack(side=tk.LEFT, padx=(0, 10))

        self.record_button = ttk.Button(
            button_frame, 
            text="Record", 
            command=self.toggle_recording
        )
        self.record_button.pack(side=tk.LEFT)

        # Output Frame
        output_frame = ttk.Frame(self.master, padding="10")
        output_frame.pack(expand=True, fill=tk.BOTH)

        output_label = ttk.Label(
            output_frame, 
            text="Generated Poetry:", 
            font=self.label_font
        )
        output_label.pack(anchor=tk.W)

        self.output_text = tk.Text(
            output_frame, 
            wrap=tk.WORD, 
            state="disabled", 
            font=self.text_font,
            padx=10,
            pady=10
        )
        self.output_text.pack(expand=True, fill=tk.BOTH)

        text_scrollbar = ttk.Scrollbar(
            output_frame, 
            orient="vertical", 
            command=self.output_text.yview
        )
        text_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.output_text.configure(yscrollcommand=text_scrollbar.set)

    def on_submit(self):
        input_text = self.input_entry.get("1.0", tk.END).strip()
        if input_text:
            output = functionality(input_text)
            self.update_output(f"{output}\n\n")
            self.input_entry.delete("1.0", tk.END)
        else:
            self.update_output("Please provide a theme for your poem.\n\n")

    def update_output(self, text):
        self.output_text.configure(state="normal")
        self.output_text.insert("1.0", text)
        self.output_text.configure(state="disabled")
        self.output_text.see("1.0")

    def toggle_recording(self):
        self.is_recording = not self.is_recording
        if self.is_recording:
            self.update_record_button_text()
        else:
            self.record_button.config(text="Record")

    def update_record_button_text(self):
        if self.is_recording:
            texts = ["Recording", "Recording.", "Recording..", "Recording..."]
            self.record_button.config(text=texts[self.record_text_index])
            self.record_text_index = (self.record_text_index + 1) % len(texts)
            self.master.after(500, self.update_record_button_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimplifiedInterface(root)
    root.mainloop()
