from flask import Flask, render_template, request
from crewai import Crew
from crew_agents import CrewAgents
from crew_tasks import CrewTasks

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        question = request.form['question']
        answer = runcrew(question) #call crew get_answer_from_model(question)
        return render_template('index.html', question=question, answer=answer)
    return render_template('index.html', question='',answer='')

def runcrew(question):
    agents = CrewAgents()
    tasks = CrewTasks()

    searcher = agents.searcher()
    editor = agents.editor()

    searcher_task = tasks.searcher_task(
        question,
        searcher
    )

    editor_task = tasks.editor_task(editor)
    
    print("test")
    crew = Crew(agents=[searcher,editor] , tasks=[searcher_task, editor_task], verbose=True )
    result = crew.kickoff()
    return result


if __name__ == '__main__':
    app.run(debug=True)