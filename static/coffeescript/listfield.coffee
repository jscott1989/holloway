# 
# This is the javascript that will turn any input with a class of .type_listfield
# into a JSON list input.
# 
# It will create a text field for inputting values, an add button, and a list of current
# values with a button to remove each one.

listfield_html = "
    <div>
        <ul class='listitems' data-bind='foreach: items'>
            <li>
                <span data-bind='text: $data'></span>
                <a href='#' data-bind='click: $parent.remove'>remove</a>
            </li>
        </ul>
        <div class='row'>
            <div class='small-10 columns'>
                <input type='text' data-bind='value: field_value'>
            </div>
            <div class='small-2 columns'>
                <button type='submit' data-bind='click: click'>Add</button>
            </div>
        </div>
    </div>
"

$ ->
    $(".type_listfield").each -> 
        $this = $(this)

        # Create/insert new list interface
        domelement = $(listfield_html).insertAfter($this)
        domelement.append($this)

        # Ensure final result is bound to the correct input
        $this.attr('data-bind', 'value: json_value')

        viewmodel =
            items: ko.observableArray()
            field_value: ko.observable("")
            click: () ->
                if (viewmodel.field_value() != "")
                    viewmodel.items.push(viewmodel.field_value())
                    viewmodel.field_value("")
            remove: (item) ->
                viewmodel.items.remove(item)

        # This has to go after the viewmodel is defined as it relies on
        # the viewmodel existing
        viewmodel.json_value = ko.computed ->
                ko.toJSON(viewmodel.items())

        ko.applyBindings(viewmodel, domelement[0])
        $this.hide()
