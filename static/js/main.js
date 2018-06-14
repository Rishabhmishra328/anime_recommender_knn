function add_anime() {
    var req = new XMLHttpRequest();
    req.onreadystatechange = function()
    {
        console.log(this.responseText);
        if(this.readyState == 4 && this.status == 200) {
            var jsonVal = JSON.parse(this.responseText);

            var selectAnimeDIV = document.getElementById('selectedAnimeListContainer');

            var containerDIV = document.createElement('div');
            containerDIV.setAttribute('class', 'selectedAnimeContainer');
            
            var img_view = document.createElement('img');
            img_view.setAttribute('src', jsonVal['image_url']);
            img_view.setAttribute('class', 'selectedAnimeImage');

            var slider_view = document.createElement('input');
            slider_view.setAttribute('type', 'range');
            slider_view.setAttribute('value', 100);
            slider_view.setAttribute('min', 1);
            slider_view.setAttribute('max', 100);
            slider_view.setAttribute('class', 'strengthslider');
            
            var name_view = document.createElement('div');
            name_view.innerText = jsonVal['name'];
            name_view.setAttribute('class', 'selectedAnimeName');
            
            containerDIV.appendChild(name_view);
            containerDIV.appendChild(img_view);
            containerDIV.appendChild(slider_view);
            
            selectAnimeDIV.appendChild(containerDIV);
        } else {
            // result.value = "Try another anime";
        }
    }

    var animeList = new Array();
    var selectAnimeDIV = document.getElementById('selectedAnimeListContainer');
    var selectedAnime = selectAnimeDIV.children;
    if(typeof selectedAnime !== undefined){
        for(var i = 0; i < selectedAnime.length; i++){
            animeList.push(selectedAnime[i].children[0].innerText);
        }
    }

    req.open('POST', '/', true);
    req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    req.send("animename=" + document.getElementById('animeinput').value + "&" + "from=" + "add" + "&" + "list=" + animeList);
}



function submit_selection() {
    var req = new XMLHttpRequest();
    var recomAnimeDIV = document.getElementById('recomAnimeListContainer');
    req.onreadystatechange = function()
    {
        if(this.readyState == 4 && this.status == 200) {
            var jsonVal = JSON.parse(this.responseText)['recom'];
            var recom = String(jsonVal).split(',');

            var selectAnimeDIV = document.getElementById('recomAnimeListContainer');
            while(selectAnimeDIV.firstChild) {
                selectAnimeDIV.removeChild(selectAnimeDIV.firstChild);
            }

            for(var i = 0; i < recom.length; i ++){

             var containerDIV = document.createElement('div');
             containerDIV.setAttribute('class', 'selectedAnimeContainer');

             var img_view = document.createElement('img');
             img_view.setAttribute('class', 'selectedAnimeImage');

             var name_view = document.createElement('div');
             name_view.setAttribute('class', 'selectedAnimeName');

             var score_view = document.createElement('div');
             score_view.setAttribute('class', 'selectedAnimeName');

             if(i % 4 == 3){
                name_view.innerText = recom[i-2]; 
                score_view.innerText = 'Score:' + recom[i-1];
                img_view.setAttribute('src', recom[i]);
                containerDIV.appendChild(name_view);
                containerDIV.appendChild(img_view);
                containerDIV.appendChild(score_view);
                selectAnimeDIV.appendChild(containerDIV);
            }
        }
            // recomAnimeDIV.innerText = recom_ids + recom_names + recom_score + recom_img_url;
        } else {
            // result.value = "Try another anime";
        }
    }

    var animeList = new Array();
    var animeStrength = new Array();
    var selectAnimeDIV = document.getElementById('selectedAnimeListContainer');
    var selectedAnime = selectAnimeDIV.children;
    if(typeof selectedAnime !== undefined){
        for(var i = 0; i < selectedAnime.length; i++){
            animeList.push(selectedAnime[i].children[0].innerText);
            animeStrength.push(selectedAnime[i].children[2].value);
        }
    }

    var numrecom = document.getElementById('numrecom').value;

    req.open('POST', '/', true);
    req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    req.send("animename=" + document.getElementById('animeinput').value + "&" + "from=" + "go" + "&" + "list=" + animeList + "&" + "strength=" + animeStrength + "&" + "num=" + numrecom);
}