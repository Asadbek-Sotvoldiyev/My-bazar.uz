(function ($){
    "use strict";

// Modalni ochish uchun funksiya
function openModal() {
    var modal = document.getElementById("cartModal");
    modal.style.display = "block";
    // Modalni 2 sekund so'ng yopish
    setTimeout(function(){
        closeModal();
        }, 2000);
}

// Modalni yopish uchun funksiya
function closeModal() {
    var modal = document.getElementById("cartModal");
    modal.style.display = "none";
    location.reload();
}


// Add to Cart tugmasi bosilganda modalni ochish
$(document).on('click', '.add-to-cart-btn', function(e){
    let nomi = document.getElementById('nomi');
    let soni = document.getElementById('soni');
    let url = $("#cartbtn").data('url');
    $.ajax(
        {
            type: "GET",
            url: url,
            data: {
                product_id: $(this).data('product-id'),
                action: 'get',
            },
            success: function(json){
                $('#prod-rasm').attr('src', json.image);
                nomi.textContent = json.name;
                soni.textContent = json.quantity;
                $('#cart_count').textContent = json.cart_len;
                console.log(json.cart_len)
                openModal();
            },
            error: function(msg, err){

            }
        }
    );
});

// Modalni yopish tugmasi


// Foydalanuvchi modalni chiqarishni rad qilsa
$(document).on('click', function(event) {
    var modal = document.getElementById("cartModal");
    if (event.target == modal) {
        closeModal();
    }
});

$(document).on('click', '#close', function(){
    closeModal();
});

$(document).on('click', '.close', function(){
    closeModal();
});


function openfModal() {
    var modal = document.getElementById("favoriteModal");
    modal.style.display = "block";
    // Modalni 2 sekund so'ng yopish
    setTimeout(function(){
        closeModal();
        }, 2000);
}


$(document).on('click', '.regular', function(e){
    e.preventDefault();
    let nomi = document.getElementById('nom');
    let narx = document.getElementById('narx');
    var product_id = $(this).data('product-id');
    let url = $("#cartbtn").data('favorite');
    $.ajax(
        {
            type: "GET",
            url: url,
            data: {
                product_id: product_id ,
                action: 'get',
            },
            success: function(json){
                $('#prod-rasmi').attr('src', json.image);
                nomi.textContent = json.name;
                narx.textContent = json.narx;
                openfModal();
            },
            error: function(msg, err){

            }
        }
    );
});

$(document).on('click', '.solid', function(e){
    e.preventDefault();
    var product_id = $(this).data('product-id');
    let url = $("#cartbtn").data('favorite-del');
    $.ajax(
        {
            type: "GET",
            url: url,
            data: {
                product_id: product_id ,
                action: 'get',
            },
            success: function(json){
                location.reload()
            },
            error: function(msg, err){

            }
        }
    );
});

})(jQuery);