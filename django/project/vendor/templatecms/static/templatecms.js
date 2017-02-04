$(document).ready(function() {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    var widget = uploadcare.Widget('[role=uploadcare-uploader]');
    widget.onChange(function(file) {
      if (file) {
        file.done(function(info) {
            var key = $('[role="uploadcare-uploader"]').data('key');
            var value = info.originalUrl;
            var data = {
                data: {}
            };
            data.data[key] = value;
            $.ajax({
                url: '/admin/templatecms/copy/api/update/',
            type: "POST",
            data: JSON.stringify(data),
            headers: {
                'X-CSRFToken': csrftoken
            },
            contentType: "application/json",
            success: function(resultData) {
                window.location.reload()
            }
            });
        });
      };
    });
    $('.tcms-btn-edit').on('click', function(event) {
        var button = $(this);
        var copy = button.data('copy');
        var key = button.data('key');
        var modal = $('#js-tcms-modal');
        modal.find('.edit-copy').replaceWith('<textarea data-key="' + key + '" name="edit-copy" class="tcms-form-control edit-copy" rows="3">' + copy + '</textarea>');
    })

    $("#editable-form").on('submit', function(event) {
        event.preventDefault();
        var $textarea = $(this).find('textarea');
        var value = $textarea.val();
        var key = $textarea.data('key');
        var data = {
            data: {}
        };
        data.data[key] = value;
        $.ajax({
            url: '/admin/templatecms/copy/api/update/',
            type: "POST",
            data: JSON.stringify(data),
            headers: {
                'X-CSRFToken': csrftoken
            },
            contentType: "application/json",
            success: function(resultData) {
                 window.location.reload()
            }
        });
    });

    $.each($('.tcms-editable'), function(i, editable) {
        var $editable = $(editable);
        var link = $editable.next('.tcms-btn-edit');
        link.offset({
            top: $editable.offset().top,
            left: $editable.offset().left - link.outerWidth() - 5
        });
    });

    if($('#editable-toolbar-toggle').siblings('a').css('display') != 'none') {
        $('body').addClass('show-edit-btns');
    }

    $('#editable-toolbar-toggle').on('click', function() {
        $('body').toggleClass('show-edit-btns');
    })
});