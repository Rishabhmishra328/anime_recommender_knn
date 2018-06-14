from flask import Flask, render_template, request, jsonify
import data_services as ds

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "POST" and request.form["from"] == "add":
        name = request.form["animename"]
        all_anime = ds.get_data()[0][:, 1]
        selected_anime = request.form["list"]
        if((name in all_anime) and (name not in selected_anime)):
            image_url = ds.get_image_link(name = name)
            return jsonify({'name': name, 'image_url': image_url})
        else:
            pass
    if request.method == "POST" and request.form["from"] == "go":

        selectedList = request.form["list"].split(",")
        selectedListStrength = request.form["strength"].split(",")
        num = request.form['num']
        ids = []
        strength = []
        for item in selectedList:
            ids.append(int(ds.get_id(item)))

        for item in selectedListStrength:
            strength.append(float(item) / 100)

        print strength, ids
        recom = ds.get_recom(suggestions = num, ids = ids, strength = strength)
        print recom
        return jsonify({'recom': recom})
    animeList = ds.get_data()[0][:, 1]
    return render_template('index.html', animelist = animeList)

if __name__ == '__main__':
    app.run(debug = True)