$ ->
    text_changed = false;
    html_changed = false;

    html_to_text = (text) ->
        text = text.replace(/<a.*?href=['"](.*?)['"]>(.*?)<\/a>/ig,"$2 ($1)")
        $("<div>" + text + "</div>").text()

    text_to_html = (text) ->
        text.replace(/\n/ig,"<br />\n")

    $('#id_text').on 'input', () ->
        if (!html_changed)
            $('#id_html').val(text_to_html($('#id_text').val()))
        text_changed = true

    $('#id_html').on 'input', () ->
        if (!text_changed)
            $('#id_text').val(html_to_text($('#id_html').val()))
        html_changed = true