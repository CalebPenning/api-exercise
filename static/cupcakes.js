const BASE_URL = 'http://127.0.0.1:5000/api'

function generateCupcakeHTML(cupcake) {
    return `
    <div data-cupcake-id=${cupcake.id}>
        <li>
            ${cupcake.flavor} | ${cupcake.size} | ${cupcake.rating}
            <button class="delete-button">X</button>
            </li>
            <img class="cupcake-img" src="${cupcake.image}" alt="no image provided">
    </div>
    `;
}

async function showInitialCupcakes() {
    const response = await axios.get(`${BASE_URL}/cupcakes`)
    console.log(response)
    for (let cakeData of response.data) {
        let newCake = $(generateCupcakeHTML(cakeData));
        $("ul").append(newCake);
    }
}

$("form").on("submit", async function (evt) {
    evt.preventDefault();
  
    let flavor = $("#flavor").val();
    let rating = $("#rating").val();
    let size = $("#size").val();
    let image = $("#image").val();
  
    const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, {
      flavor,
      rating,
      size,
      image
    });
  
    let newCupcake = $(generateCupcakeHTML(newCupcakeResponse.data));
    $("#cake-list").append(newCupcake);
    $("form").trigger("reset");
  });
  
$("#cake-list").on("click", ".delete-button", async function(e) {
  e.preventDefault();
  let $cake = $(e.target).closest("div");
  let $cakeId = $cake.attr("data-cupcake-id");

  await axios.delete(`${BASE_URL}/cupcakes/${$cakeId}`);
  $cake.remove();
})

showInitialCupcakes();
