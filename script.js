async function getWeather() {

    const city = document.getElementById("city").value;

    const apiKey = "d7a617415fc86e907ea51dce2aa73dbb";

    const url =
    `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    try {

        const response = await fetch(url);

        const data = await response.json();

        if (data.cod == "404") {
            alert("City not found");
            return;
        }

        document.getElementById("weatherCard").style.display = "block";

        document.getElementById("cityName").innerText =
        data.name;

        document.getElementById("temperature").innerText =
        `Temperature: ${data.main.temp} °C`;

        document.getElementById("humidity").innerText =
        `Humidity: ${data.main.humidity}%`;

        document.getElementById("condition").innerText =
        `Condition: ${data.weather[0].main}`;

    }

    catch(error) {
        alert("Something went wrong");
        console.log(error);
    }

}