async function uploadImage() {
  const input = document.getElementById("imageInput");
  const output = document.getElementById("output");

  if (!input.files[0]) {
    alert("Please select an image file first.");
    return;
  }

  const formData = new FormData();
  formData.append("file", input.files[0]);

  output.textContent = "Loading...";

  try {
    const response = await fetch("http://localhost:8000/predict", {
      method: "POST",
      body: formData
    });
    const tags = await response.json();
    output.textContent = tags.join("\n");
  } catch (err) {
    output.textContent = "Error: " + err.message;
  }
}

