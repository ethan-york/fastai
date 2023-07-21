<html>
    <head>
        This is a test!
    </head>

  <body>
    <input id="photo" type ="file" id="load">
    <!-- <button id="button1" class="btn btn-primary" type="submit" onclick="loaded">Get Predictions</button> -->
    <br>
    <div id="results"></div>
    <br>
  </body>
  <script>
    async function loaded(reader) {
        const response = await fetch("https://ethan-york-bear-identifier.hf.space/api/predict/",{
            method:"POST",
            body: JSON.stringify({"data":[reader.result]}),
            headers: {
                "Content-Type": "application/json"}
        });
        const json = await response.json();
        const label = json['data'][0]['confidences'][0]['label'];
        results.innerHTML = `<br/><img src="${reader.result}" width="300" /><br/><p>${label}</p>`;
    }
    function read() {
        const reader = new FileReader();
        reader.addEventListener("load", () => loaded(reader))
        reader.readAsDataURL(photo.files[0]);
    }
    photo.addEventListener('input',read)
  </script>
</html>