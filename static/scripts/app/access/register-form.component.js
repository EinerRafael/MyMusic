angular.module('Access').component("registerForm", {
    template: `
		<form class="form-horizontal col-md-6" ng-submit="$ctrl.register()">
		  <fieldset>
		    <legend>Registrarse</legend>
		    <div class="form-group">
		      <label for="nameInput" class="col-lg-2 control-label">Nombres</label>
		      <div class="col-lg-10">
		        <input class="form-control" id="nameInput" placeholder="Nombres" type="text" required ng-model="$ctrl.name">
		      </div>
		    </div>
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
		<div class="alert alert-dismissible alert-success" ng-repeat='message in $ctrl.messages'>
		  <button type="button" class="close" data-dismiss="alert">&times;</button>
		 <strong>{{message.message}}</strong>
		 <span>{{message.description}}</span>
		</div>
		<br />
		<div class="alert alert-dismissible alert-danger" ng-repeat='error in $ctrl.errors'>
		  <button type="button" class="close" data-dismiss="alert">&times;</button>
		 <strong>{{error.message}}</strong>
		 <span>{{error.description}}</span>
		</div>
	`,
    controller: ['Consumer', function(Consumer) {
        var self = this;
        self.name = "";
        self.email = "";
        self.passsword = "";
        self.errors = [];
        self.messages = [];


        self.register = function() {
            var objSend = {
                "first_name": self.name,
                "last_name": "NA",
                "email": self.email,
                "password": self.password,
                "image": "None"
            };
            Consumer.register(objSend).then(function(resp) {
                console.log(resp);
                self.messages.push({
                	'title': "Exito",
                	'description': "Registro exitoso"
                });
                self.name = "";
                self.email = "";
                self.password = "";
            }).catch(function(resp) {
                if (resp.status == 400) {
                    self.errors = [];
                    self.errors.push({
                        title: "No se ha podido registrar",
                        description: "Verifique su email ó ya hay un usuario con ese email"
                    })
                }

            })
            return false;
        }

    }]
});
