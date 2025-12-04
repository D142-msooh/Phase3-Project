import sqlite3
from datetime import datetime

conn = sqlite3.connect('Opportunity.db')
cursor = conn.cursor()