(function() {
    function change_record_status(status, ids, row = false) {
        $.post('/status', {status: status, ids: ids}, function(res) {
            if (!res.status) return;
            if (row) {
                row.remove();
            } else {
                location.reload();
            }
        });
    };

    $('.btn-current').click(function() {
        change_record_status('current', [$(this).attr('data-row')], $(this).closest('tr'));
    });

    $('.btn-icebox').click(function() {
        change_record_status('icebox', [$(this).attr('data-row')], $(this).closest('tr'));
    });

    $('.btn-archive').click(function() {
        change_record_status('archive', [$(this).attr('data-row')], $(this).closest('tr'));
    });

    $('.btn-toggle-visible').click(function() {
        let btn = $(this);
        $.post('/toggle_visible', {id: btn.attr('data-row')}, function(res) {
            if (! res.status) return;
            if (res.visible) {
                btn.removeClass('btn-warning').addClass('btn-success').html('hide');
            } else {
                btn.removeClass('btn-success').addClass('btn-warning').html('show');
            }
        });
    });

    $('#btn-archive').click(function() {
        let ids = []
        $('.til-post').each(function(i, obj) {
            ids.push($(obj).attr('id'));
        });
        if (ids.length > 0) {
            change_record_status('archive', ids);
        }
    });

}());