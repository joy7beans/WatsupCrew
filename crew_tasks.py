from crewai import Task
from textwrap import dedent

class CrewTasks():

    def searcher_task(self, question, agent):
        return Task(description= dedent(f"""{question}.\
                                        Only use the input provided as search query in the tool. Do not add any additional words. \
                                        Use input query as absolute search query. """),
                    expected_output='JSON with Title, Summary and weblink, publish date and source with 5 records.',
                    agent=agent
    )

    def editor_task(self,agent):
        return Task(
            description='Summarize the news articles in the JSON. \
                         You should only summarize using the news provided by by the colleague. \
                         The final result should only be a summary of the article. ',
            expected_output='An Article with summary of the news.  ',
            agent=agent  
        )
