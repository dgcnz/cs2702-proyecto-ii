
function get_new(id){

    var message = JSON.stringify({
        "id": id,
    });

    $.ajax({
        url:'/get-new-by-id',
        type:'POST',
        contentType: 'application/json',
        data : message,
        dataType:'json',
        success: function(response){
            console.log(response);  
            var opened = window.open("");
            opened.document.write(`
            <html><head><title>${response.title}</title></head>
                <body>
                    <h1>${response.title}</h1>
                    <h3>Id: ${response.id}</h3>
                    <h3>Date: ${response.date}</h3>
                    <h3>Author: ${response.author}</h3>
                    <p>${response.content}</p>
                </body>
            </html>
            `);
            opened.document.close();
        },
        error: function(response){
            alert("Error de conexión!");
        }
    });
}

function buscar(){
    var cantidad = $('#numElement').val();

    var words = $('#searchBar').val();
    var k_value = $('#kBar').val();

    var message = JSON.stringify({
        "words": words,
        "k_value": k_value
    });
    loading();
    $.ajax({
        url:'/get-news',
        type:'POST',
        contentType: 'application/json',
        data : message,
        dataType:'json',
        success: function(response){
            $("#loading").hide();
            $("#resultados").html("");

            $.each(response, function(key, value) {
                console.log(value);
                var parsedDate = new Date(value.date);
                var time = parsedDate.toLocaleTimeString(); 
                var date = parsedDate.toLocaleDateString('en-GB'); 
                
                var string = `
                    <article class='card mb-4' onclick="get_new(${value.id})">
                        <header class='card__header' style="height:100px;">
                            <div class='card__userinfo'>
                                <h2 style="display: inline-block; font-size: 22px;" class='card__name'>${value.title}</h2>
                                &nbsp;
                                <span style="display: inline-block;" class='card__date'>${value.id}</span> 
                                <span>•</span>
                                <span style="display: inline-block;" class='card__date'>${value.date}</span> 
                            </div>
                        </header> 
                        <class='card__text'>
                            <p class='card__paragraph'>${value.content}</p>  
                        <footer class='card__footer'>
                            <svg class="h-6 w-6 text-gray-500"  fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>  
                            <svg class="h-6 w-6" :class="{'text-gray-500': tweet.hasBeenRetweeted == false, 'text-green-500': tweet.hasBeenRetweeted == true }"  fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"/></svg>  
                            <svg x-show="tweet.hasBeenLiked == false" class="h-6 w-6 text-gray-500"  fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg>
                            <svg class="h-6 w-6 text-gray-500"  fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12"/></svg>
                        </footer>
                </article>
                `
                $("#resultados").append(string);
            });
        },
        error: function(response){
            alert("Error de conexión!");
        }
    });
}

$("#loading").hide();

function loading(){
    $("#loading").show();
}