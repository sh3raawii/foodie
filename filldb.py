import xlrd
from foodie_app import create_app
from foodie_app.models import Ingredient, db

app = create_app()

with app.app_context():
    db.session.query(Ingredient).delete()
    db.session.commit()
    wb = xlrd.open_workbook('data.xlsx')
    sh = wb.sheet_by_name('Sheet1')
    for rownum in range(2, sh.nrows):
        ingredient = Ingredient(name=sh.row_values(rownum)[0].lower(), gwp=float(sh.row_values(rownum)[1]))
        db.session.add(ingredient)
    db.session.commit()