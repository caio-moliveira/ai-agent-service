import textwrap
from crewai import Flow
from crewai.flow.flow import listen, start
import logging
from lead_scoring_crew import lead_scoring_crew
from email_writing_crew import email_writing_crew


class SalesPipeline(Flow):
    @start()
    def fetch_leads(self):
        # Pull our leads from the database
        leads = [
            {
                "lead_data": {
                    "name": "Kwasi Ankomah",
                    "job_title": "Architect",
                    "company": "SambaNova",
                    "email": "kwasi@samaba.com",
                    "use_case": "Using AI Agents to do better data enrichment.",
                },
            },
        ]
        return leads

    @listen(fetch_leads)
    def score_leads(self, leads):
        scores = lead_scoring_crew.kickoff_for_each(leads)
        self.state["score_crews_results"] = scores
        return scores

    @listen(score_leads)
    def store_leads_score(self, scores):
        # Here we would store the scores in the database
        return scores

    @listen(score_leads)
    def filter_leads(self, scores):
        return [score for score in scores if score["lead_score"].score > 70]

    @listen(filter_leads)
    def write_email(self, leads):
        scored_leads = [lead.to_dict() for lead in leads]
        emails = email_writing_crew.kickoff_for_each(scored_leads)
        return emails

    @listen(write_email)
    async def send_email(self, emails):
        # Here we would send the emails to the leads
        return emails


flow = SalesPipeline()


if __name__ == "__main__":
    emails = flow.kickoff()
    logging.info(f"Final Emails Sent: {emails}")

    result_text = emails[0].raw
    wrapped_text = textwrap.fill(result_text, width=80)
    print(wrapped_text)
