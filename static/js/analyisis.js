function analyzeDNA() {
    const analysisForm = document.getElementById("analysis-form");
    const analysisResult = document.getElementById("analysisResult");

    const dnaSequence = document.getElementById("dnaInput");

    fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-type':'application/json', 
            'Accept':'application/json'
        },
        body: JSON.stringify({ dna_sequence: dnaSequence.value }),
    })
    .then(response => response.json())
    .then(data => {
        dnaSequence.textContent = "";
        analysisResult.style.visibility = "visible";
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function downloadResults(){
    fetch('/download', {
        method: 'GET',
    })
    .then(data => {
        
    })
    .catch(error => {
        console.error('Error:', error);
    });
}