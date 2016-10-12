angular.module('Home').component("homeView", {
    template: `
		<h3>{{$ctrl.user.fullName()}}</h3>
        <span>{{$ctrl.user.email}}</span>
        <br />
        <a href="#" class="btn btn-primary btn-lg">Canciones</a>
        <a href="#" class="btn btn-success btn-lg">PlayList</a>
    `,
    controller: ['Consumer', 'Storage', '$location', 'Config', function(Consumer, Storage, $location, Config) {
        var self = this;
        var channel;

        function initialize() {
            if (!Storage.hasSession()) {
                $location.path("/index");
            }
            self.session = Storage.getSession();
            self.user = self.session.user;
            self.user.fullName = function() {
                return this.first_name + " " + this.last_name;
            }

            pusher = new Pusher(Config.pusher.API_KEY, {});
            channel = pusher.subscribe(Config.pusher.USER_CHANNEL.replace('{user}', self.user.id));

            channel.bind(Config.pusher.EVENT_SONG_RATE, onRateSound);
            channel.bind(Config.pusher.EVENT_PLAYLIST_RATE, onRatePlayList);
        }

        function onRateSound(data) {
            console.info('Han calificado un cacion', data.message);
        }

        function onRatePlayList(data) {
            console.info('Han calificado una playlist ', data.message);
        }

        initialize();
    }]
});
