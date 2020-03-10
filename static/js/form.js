$('#id_first_name').bind({
  focusin: function() {
    $('#autocomplete_select').css('display', 'block');
  },
});

$('#id_first_name').keyup(function(){
    var input_text = $('#id_first_name').val();
    if(input_text.length){
        $('#autocomplete_select').empty();

        $.ajax({
            url:"/autocomplete/",
            data:{
                q: input_text
            },
            success:onAjaxSuccess,
            dataType:'json'
        });
    }

    function onAjaxSuccess(data)
    {
        if(data['results'].length){
            var options = '';
            
            data['results'].forEach(function(item, i, arr) {
                console.log(item)
                options += '<li class="list-group-item">' + item['text'] + ' <a href="./add_employee/' + item['id'] + '/">+</a></li>'
            })
            $('#autocomplete_select').append(options);
        }
    }
});
