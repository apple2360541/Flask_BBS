var base = {
    'get': function (args) {
        args['method'] = 'get';
        this.ajax(args);
    },
    'post': function (args) {
        args['method'] = 'post';
        this.ajax(args)
    },
    'ajax': function (args) {
        this._ajaxSetup(args);
        $.ajax(args);
    },
    '_ajaxSetup': function (args) {
        $.ajaxSetup({
            'beforeSend': function (xhr, settings) {

                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    var csrf_token = $('meta[name=csrf_token]').attr('content');
                    xhr.setRequestHeader("X-CSRFToken", csrf_token)
                }
            }
        })
    }
};