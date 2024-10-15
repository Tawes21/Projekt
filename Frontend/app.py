from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="Tawes",
        password="",
        database="klasse_und_items",
    )


def get_item():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("Select SLOT, SOURCE From slot_drop")
    items = cursor.fetchall()
    cursor.close()
    connection.close()
    return items


@app.route("/")
def index():
    items = get_item()
    return render_template("index.html", items=items)


@app.route("/submit", methods=["POST"])
def submit():
    source_values = request.form.to_dict("source")

    connection = get_db_connection()
    cursor = connection.cursor()
    for index, source_values in source_values.items():
        if source_values:
            slot_number = index.split("_")[1]

            cursor.execute(
                "UPDATE slot_drop SET SOURCE = %s WHERE ID_ITEMSLOT = %s",
                (source_values, str(slot_number)),
            )

    connection.commit()
    cursor.close()
    connection.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
