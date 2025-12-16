from fastapi import FastAPI
from app.config.database import Base, engine
from app.routers import invoices, report  # include other routers as needed

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(invoices.router)
app.include_router(report.router)
