import csv

from market import app, db
from market.models.item import Item


@app.cli.command("add_items")
def add_items():
    filename = './ferbarmarket/web/market/csv/items.csv'
    with open(filename, mode='r') as f:
        csv_file = csv.reader(f)
        for i in csv_file:
            item = Item(name=i[0],price=i[1], barcode=i[2], description= i[3])
            db.session.add(item)
            db.session.commit()
        print('Data was added successfully')
@app.cli.command("create_tables")
def create_tables():
    db.create_all()
