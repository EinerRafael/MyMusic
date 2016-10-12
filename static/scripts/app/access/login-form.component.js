angular.module('Access').component("loginForm", {
    template: `
		<form class="form-horizontal col-md-6" ng-submit="$ctrl.login()">
		  <fieldset>
		    <legend>Ingresar</legend>
		    <div class="form-group">
		      <label for="inputEmail" class="col-lg-2 control-label">Email</label>
		      <div class="col-lg-10">
		        <input class="form-control" id="inputEmail" placeholder="Email" type="email" required ng-model="$ctrl.email">
		      </div>
		    </div>
		    <div class="form-group">
		      <label for="inputPassword" class="col-lg-2 control-label">Password</label>
		      <div class="col-lg-10">
		        <input class="form-control" id="inputPassword" placeholder="Password" type="password" required ng-model="$ctrl.passsword">
		      </div>
		    </div>
		    <div class="form-group">
		      <div class="col-lg-10 col-lg-offset-2">
		        <a href="#!/home" class="btn btn-default">Volver</a>
		        <button type="submit" class="btn btn-primary">Ingresar</button>
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
    controller: ['Consumer', 'Storage', '$location', function(Consumer, Storage, $location) {
        var self = this;
        self.email = "";
        self.passsword = "";
        self.errors = [];


        self.login = function() {
            var objSend = {
                "username": self.email,
                "password": self.passsword
            };
            Consumer.login(objSend).then(function(resp) {
            	Storage.setSession(resp.data);
            	$location.path('/home');
            }).catch(function(resp) {
                if (resp.status == 400) {
                	self.errors = [];
                    self.errors.push({
                        title: "No se ha podido iniciar sesión",
                        description: "Credenciales no Validas"
                    })
                }

            })
            return false;
        }

    }]
});
