#!/usr/bin/env python
from email_automation.crew import EmailAutomationCrew
import agentops

agentops.init()


def run():
    inputs = {
        "notes": """
        # Client Meeting Notes - Feedback Session with Quantum Solutions

        ## Date: 4/20/2024

        ## Attendees
        - Founder (Our Team)
        - Head of Product Development (Our Team)
        - CTO, Quantum Solutions
        - Marketing Director, Quantum Solutions

        ## Feedback and Action Items

        ### Engineering Team
        - **Real-Time Analytics Optimization for Short-Form Content:**
        - Feedback noted significant latency during peak upload times on TikTok and Instagram, specifically with video processing taking over 5 seconds.
        - **Action:** Reduce processing time by 30%. Implement multi-threading in the video processing algorithm and upgrade server hardware to handle higher loads. Engineering to complete changes and benchmark performance by next Friday.

        ### Data Security Enhancements
        - Client expressed concerns about vulnerability due to outdated encryption libraries used in data storage for content creators.
        - **Action:** Upgrade all encryption libraries to the latest stable versions. Specifically, update OpenSSL to version 1.1.1h to address known vulnerabilities. Security Team to audit current encryption practices and complete updates by the end of the month.

        ### Product Development
        - **User Interface Redesign for Content Creators:**
        - Feedback highlighted that the dashboard's navigation is confusing, particularly the analytics section which takes multiple clicks to access.
        - **Action:** Redesign the dashboard to ensure that key analytics are accessible within two clicks from the main screen. Design Team to collaborate with UX specialists to create a more intuitive interface and present initial mockups in two weeks.

        ### Marketing Team
        - **Promotion of Advanced Analytics Features:**
        - Advanced features like real-time engagement tracking are underutilized because they are not prominently featured in promotional materials.
        - **Action:** Create a new marketing campaign focused on real-time engagement benefits, including detailed case studies and user testimonials that showcase the improvements in user engagement metrics. Marketing to launch the campaign by next Wednesday.

        ### Additional Features Suggested
        - There is a demand for a scheduling tool that adjusts posting times dynamically based on predictive analytics of user engagement patterns.
        - **Action:** Initiate a feasibility study for developing a 'Smart Scheduler' feature that integrates with existing analytics to recommend optimal posting times. Product team to present a research report and a prototype plan in one month.

        ## General Observations
        - Quantum Solutions is keen to enhance their service offerings to better meet the needs of content creators specializing in short-form platforms.
        - There is a strong desire for clearer guidance on how to effectively utilize the platform's features.

        ## Next Steps
        - Each team lead to outline specific tasks for their teams based on today’s feedback.
        - Organize a follow-up meeting with Quantum Solutions in one month to evaluate the progress on these action points and adjust the project scope if necessary.

        """,
        "company_background": """
            # Quantum Solutions Company Background

            ## Overview
            Founded in 2022, Quantum Solutions specializes in providing cutting-edge marketing and analytics tools tailored for short-form content creators on platforms like YouTube Shorts, Instagram, and TikTok. By leveraging advanced analytics and automation, Quantum helps content creators optimize their reach and engagement effectively and efficiently.

            ## Company Structure

            ### Engineering Department
            - **Head of Engineering:** Alex Mercer
            - **Responsibilities:** Develops and enhances software solutions focused on optimizing video content analytics and distribution algorithms.
            - **Contact:** alex.mercer@quantumsolutions.tech

            ### Marketing Department
            - **Director of Marketing:** Samantha Reed
            - **Responsibilities:** Manages marketing strategies tailored to the unique demands of short-form content platforms, overseeing campaign effectiveness and influencer partnerships.
            - **Contact:** samantha.reed@quantumsolutions.tech

            ### Product Development
            - **Head of Product Development:** Jamie Lawson
            - **Responsibilities:** Leads the innovation and feature enhancement of tools designed to improve content visibility and engagement metrics for short-form videos.
            - **Contact:** jamie.lawson@quantumsolutions.tech

            ### Data Security Team
            - **Chief Security Officer:** Nina Patel
            - **Responsibilities:** Ensures the security of data analytics and content creator information, implementing top-tier security measures and compliance standards.
            - **Contact:** nina.patel@quantumsolutions.tech

            ### Customer Support and Implementation
            - **Head of Customer Support:** Carlos Gomez
            - **Responsibilities:** Provides tailored support to content creators, assisting with the implementation of analytics tools and resolving technical issues swiftly to maintain content production schedules.
            - **Contact:** carlos.gomez@quantumsolutions.tech

            ## Key Products
            - **Quantum Engage:** An analytics platform that provides real-time insights into video performance across multiple short-form content platforms.
            - **Quantum Reach:** Automates content distribution and optimizes posting schedules to maximize viewer engagement and retention.

            ## Recent Challenges
            With the rapid evolution of short-form content platforms, Quantum Solutions has faced the need to continuously adapt and improve its analytics and automation algorithms to keep pace with changing content trends and platform algorithms.

            ## Strategic Goals
            - Develop state-of-the-art features that allow creators to dynamically adjust their content strategies based on real-time feedback.
            - Expand the company’s reach by forming strategic partnerships with major content platforms and influencer agencies.

            ## Contact for Strategic Partnerships and Major Initiatives
            - **CEO:** Rachel Torres
            - **Email:** rachel.torres@quantumsolutions.tech

        """
    }
    EmailAutomationCrew().crew().kickoff(inputs=inputs)
