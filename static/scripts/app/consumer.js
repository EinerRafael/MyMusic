angular.module("Consumer", ['ngRoute']).factory("Consumer", ['$http', function($http) {
    var urls = {
        'login': "/api-token-auth/",
        'register': "/api/users/"
    }
    return {
        'login': function(data) {
            return $http({
                method: 'POST',
                data: data,
                url: urls.login,
                headers: {
                	'Content-Type': "application/json"
                }
            });
        },
        'register': function(data) {
            return $http({
                method: 'POST',
                data: data,
                url: urls.register,
                headers: {
                	'Content-Type': "application/json"
                }
            });
        }
    }
}])
