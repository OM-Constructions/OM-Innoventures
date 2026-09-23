"""
Seed real Data Science, Analytics & Engineering projects from ~/Videos into OM Innoventures Database.
"""

import os
import sys
import datetime

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backend'))

from app.database import SessionLocal
from app.models import User, Project, Review
from app.services.auth_service import hash_password

REAL_PROJECTS = [
    {
        "title": "Air Quality Analysis & PM2.5 Prediction Model",
        "service_slug": "data-science",
        "summary": "Environmental data science pipeline evaluating particulate matter concentrations and forecasting PM2.5 levels using statistical regression and time-series models.",
        "file": "Air Quality Analysis & PM2.5 Prediction Data Scienceproject.pdf",
        "type": "spec"
    },
    {
        "title": "Customer Churn Prediction Engine",
        "service_slug": "data-science",
        "summary": "Predictive classification system identifying customer attrition indicators and behavior patterns to optimize retention strategies and lifetime value.",
        "file": "Customer Churn Prediction Data science project.pdf",
        "type": "report"
    },
    {
        "title": "Sales Forecasting & Trend Modeling via Linear Regression",
        "service_slug": "data-analytics-bi",
        "summary": "Multi-variable statistical forecasting model estimating quarterly enterprise revenue trajectory based on historical performance indicators.",
        "file": "Data Science Project Sales Forecasting using Linear Regression Model.pdf",
        "type": "report"
    },
    {
        "title": "Data Analyst OMNI Enterprise Solutions",
        "service_slug": "data-analytics-bi",
        "summary": "Comprehensive data analysis solution with structured data cleaning, exploratory visual analytics, and business intelligence metrics.",
        "file": "Data analyst OMNI Assignment solutions.pdf",
        "type": "deliverable"
    },
    {
        "title": "Financial Data Analysis with Scikit-Learn & Pandas",
        "service_slug": "finance-accounting",
        "summary": "Quantitative financial analytics pipeline for risk profiling, portfolio asset distributions, and variance metrics using Python statistical libraries.",
        "file": "Financial Data analysis using Scikit-Learn & Pandas.pdf",
        "type": "report"
    },
    {
        "title": "Corporate Financial Performance & Cashflow Analytics",
        "service_slug": "finance-accounting",
        "summary": "Financial statement analysis, ratio evaluations, and revenue breakdown analytics for operational decision support.",
        "file": "Financial data analysis small project.pdf",
        "type": "report"
    },
    {
        "title": "Fraud Detection Machine Learning System",
        "service_slug": "cybersecurity",
        "summary": "Supervised anomaly detection and classification pipeline for real-time transaction screening and fraudulent pattern identification.",
        "file": "Fraud Detection Data Science Project.pdf",
        "type": "spec"
    },
    {
        "title": "HR & Workforce Operations Analytics",
        "service_slug": "data-analytics-bi",
        "summary": "Workforce attrition, performance distribution, and talent acquisition metrics modeled into an operational HR intelligence dashboard.",
        "file": "HR Data Analysis small project.pdf",
        "type": "report"
    },
    {
        "title": "House Price Valuation & Real Estate Prediction Model",
        "service_slug": "data-science",
        "summary": "Regression pipeline estimating residential real estate market valuations based on spatial attributes, square footage, and neighborhood metrics.",
        "file": "House Price Prediction Data Science Project.pdf",
        "type": "deliverable"
    },
    {
        "title": "Loan Eligibility Risk Assessment & Classification",
        "service_slug": "finance-accounting",
        "summary": "Credit risk decision-tree and gradient boosted classification model determining loan approval eligibility from applicant credit profiles.",
        "file": "Loan Eligibility Prediction Data Science project.pdf",
        "type": "spec"
    },
    {
        "title": "E-Commerce Product Recommendation Engine",
        "service_slug": "ai-ml-solutions",
        "summary": "Collaborative and content-based recommendation algorithms delivering personalized product feeds to boost digital conversion rates.",
        "file": "Product Recommendation System E-commerce Data Science Project.pdf",
        "type": "deliverable"
    },
    {
        "title": "Sales Database Schema & SQL Query Analytics Hub",
        "service_slug": "data-analytics-bi",
        "summary": "Relational SQL database architecture with optimized aggregation queries, store performance indexing, and customer purchasing metrics.",
        "file": "Sales dataset sql mini project.sql",
        "type": "deliverable"
    },
    {
        "title": "Excel Sales Analytics & Multi-Tier Pivot Modeling",
        "service_slug": "data-analytics-bi",
        "summary": "Advanced spreadsheet dashboard featuring automated pivot tables, KPI calculations, and executive visual reporting charts.",
        "file": "sample_sales_data analysed by EXCEL.pdf",
        "type": "report"
    }
]

def seed_projects():
    db = SessionLocal()
    try:
        # 1. Ensure verified client exists
        client = db.query(User).filter(User.email == "client@ominnoventures.ai").first()
        if not client:
            client = User(
                name="OM Innoventures Client",
                email="client@ominnoventures.ai",
                password_hash=hash_password("Client123!"),
                is_verified=True
            )
            db.add(client)
            db.commit()
            db.refresh(client)
            print(f"Created client account: {client.email}")

        # 2. Clear old projects
        db.query(Review).delete()
        db.query(Project).delete()
        db.commit()
        print("Cleared previous projects.")

        # 3. Insert real projects
        now = datetime.datetime.utcnow()
        for i, item in enumerate(REAL_PROJECTS):
            proj = Project(
                user_id=client.id,
                title=item["title"],
                service_slug=item["service_slug"],
                summary=item["summary"],
                status="published",
                completed_at=now - datetime.timedelta(days=i*3)
            )
            db.add(proj)
            db.commit()
            db.refresh(proj)

            # Add verified review
            review = Review(
                project_id=proj.id,
                user_id=client.id,
                rating=5,
                review_text=f"Excellent deliverable. {item['summary']}",
                status="approved",
                reviewed_at=now
            )
            db.add(review)
            db.commit()
            print(f"✓ Added Real Project: {proj.title}")

        print(f"\n Successfully added {len(REAL_PROJECTS)} real projects into the database!")

    except Exception as e:
        db.rollback()
        print(f"Error seeding projects: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_projects()
