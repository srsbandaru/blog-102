$.ajaxSetup({
    beforeSend: function beforeSend(xhr, settings) {
        function getCookie(name) {
            let cookieValue = null;


            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');

                for (let i = 0; i < cookies.length; i += 1) {
                    const cookie = jQuery.trim(cookies[i]);

                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (`${name}=`)) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }

            return cookieValue;
        }

        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        }
    },
});

$(document).on('click', '.js-follow', function(e){
    e.preventDefault();
    const action = $(this).attr("data-action");
   
    $.ajax({
        type: 'POST',
        url: $(this).data("url"),
        data: {
            action : action,
            id : $(this).data("id"),
        },
        success: (data) => {
            // console.log(data)
            $(".js-follow-text").text(data.wording)
            if (action == "follow"){
                // Change wording to unfollow
                $(this).attr("data-action","unfollow")
            }
            else {
                // Change wording to follow
                $(this).attr("data-action","follow")
            }
        },
        error: (error) => {
            console.warn(error)
        }
    });
    
    setTimeout(function() {
        location.reload();
    }, 1000);
})