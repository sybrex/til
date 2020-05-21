(function() {
    $('.btn-current').click(function() {
        $.post('/status', {status: 'current', ids: $(this).attr('data-row')}, function(res) {
            if (res.status) $(this).closest('tr').remove();
        });
    })

    $('.btn-icebox').click(function() {
        $.post('/status', {status: 'icebox', ids: $(this).attr('data-row')}, function(res) {
            if (res.status) $(this).closest('tr').remove();
        });
    })

    $('#btn-archive').click(function() {
        let ids = []
        $('.til-post').each(function(obj) {
            console.log(obj);
        });
    })

}());