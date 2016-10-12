angular.module('Home').component("songForm", {
    template: `
        <h3>Nueva Canción</h3>
        <h4>{{$ctrl.user.fullName()}}</h4>
        <span>{{$ctrl.user.email}}</span>
        <form class="form-horizontal col-md-6" ng-submit="$ctrl.register()">
          <fieldset>
            <legend>Agregar Canción</legend>
            <div class="form-group">
              <label for="inputEmail" class="col-lg-2 control-label">Nombre</label>
              <div class="col-lg-10">
                <input class="form-control" id="inputEmail" placeholder="Nombre" type="text" required ng-model="$ctrl.name">
              </div>
            </div>
            <div class="form-group">
              <label for="inputEmail" class="col-lg-2 control-label">Artista</label>
              <div class="col-lg-10">
                <input class="form-control" id="inputEmail" placeholder="Artista" type="text" required ng-model="$ctrl.artist">
              </div>
            </div>
            <div class="form-group">
              <label for="inputEmail" class="col-lg-2 control-label">Album</label>
              <div class="col-lg-10">
                <input class="form-control" id="inputEmail" placeholder="Album" type="text" required ng-model="$ctrl.album">
              </div>
            </div>
            <div class="form-group">
              <label for="inputEmail" class="col-lg-2 control-label">Duración</label>
              <div class="col-lg-10">
                <input class="form-control" id="inputEmail" placeholder="Duración" type="number" min="1" required ng-model="$ctrl.duration">
              </div>
            </div>
            <div class="form-group">
              <div class="col-lg-10 col-lg-offset-2">
                <a href="#!/home/songs/" class="btn btn-default">Volver</a>
                <button type="submit" class="btn btn-primary">Agregar</button>
              </div>
            </div>
           </fieldset>
        </form>
        <br />
        <div class="alert alert-dismissible alert-danger" ng-repeat='error in $ctrl.errors'>
          <button type="button" class="close" data-dismiss="alert">&times;</button>
         <strong>{{error.message}}</strong>
         <span>{{error.description}}</span>
        </div>    
    `,
    controller: ['Consumer', 'Storage', '$location', 'Config', function(Consumer, Storage, $location, Config) {
        var self = this;
        self.name = "";
        self.artist = "";
        self.album = "";
        self.duration = 1;

        function initialize() {
            if (!Storage.hasSession()) {
                $location.path("/index");
            }
            self.session = Storage.getSession();
            self.user = self.session.user;
            self.user.fullName = function() {
                return this.first_name + " " + this.last_name;
            }
        }

        self.register = function() {
            var objSend = {
                "name": self.name,
                "album": self.name,
                "artist": self.artist,
                "duration": self.duration,
                "creator": self.user.id,
                "audio_path": "None"
            };
            Consumer.add_song(objSend, Storage.getToken()).then(function(resp){
                $location.path("/home/songs/");
            });
            return false;
        }

        initialize();
    }]
});
