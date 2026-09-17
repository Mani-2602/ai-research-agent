import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilyAnswer

load_dotenv()

# 1. Initialize Stable Brain (Using Groq's active production model ID) & Search Tools
llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0.2)
search_tool = TavilyAnswer()

def run_research_agent(topic):
    print("🕵️‍♂️ Researcher Agent: Scanning global databases and web directories...")
    
    # Executing internet search tool natively
    search_query = f"Latest advancements breakthroughs trends and timeline for {topic}"
    raw_research_notes = search_tool.run(search_query)
    
    print("✍️ Writer Agent: Synthesizing data points into executive summary structure...")
    
    # Formulating the orchestration instructions for the writer agent
    writer_prompt = f"""
    You are an expert Technical Content Strategist. Your task is to take the following raw web research notes
    and structure them into a highly professional, comprehensive industry intelligence report.
    
    Research Target Topic: {topic}
    Raw Research Findings: {raw_research_notes}
    
    Provide a beautiful, standalone report structured perfectly in Markdown.
    Include headers for: Executive Summary, Key Technical Innovations, Project Timelines/Trends, and Future Market Outlook.
    Ensure it looks clean, articulate, and completely corporate-grade.
    """
    
    # Invoking the LLM brain to compile the final brief document
    response = llm.invoke(writer_prompt)
    return response.content
