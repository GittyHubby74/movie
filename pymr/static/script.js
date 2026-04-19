async function getRecommendations() {
    const movie = document.getElementById("movieInput").value;
    const resultsDiv = document.getElementById("results");

    // Clear previous results
    resultsDiv.innerHTML = "Loading...";

    try {
        const response = await fetch("/recommend", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ movie: movie })
        });

        const data = await response.json();

        // Clear loading text
        resultsDiv.innerHTML = "";

        if (data.recommendations.length === 0) {
            resultsDiv.innerHTML = "<p>No recommendations found.</p>";
            return;
        }

        data.recommendations.forEach((m, index) => {
            const div = document.createElement("div");
            div.className = "movie";
            div.innerText = (index + 1) + ". " + m;
            resultsDiv.appendChild(div);
        });

    } catch (error) {
        resultsDiv.innerHTML = "<p>Error getting recommendations.</p>";
        console.error(error);
    }
}