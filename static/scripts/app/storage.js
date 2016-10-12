angular.module("Storage", ['ngRoute']).factory("Storage", [function() {
	var session_storage = sessionStorage;

	return {
		'setSession': function(obj){
			session_storage.setItem('session', JSON.stringify(obj))
		},
		'getSession': function(){
		 	var sess = session_storage.getItem('session');
		 	if (sess) {
		 		return JSON.parse(sess);
		 	}
		 	return undefined;
		},
		'hasSession': function(){
			if (this.getSession()) {
				return true;
			}
			return false;
		}
	}
}]);