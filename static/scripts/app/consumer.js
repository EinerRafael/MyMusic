angular.module("Consumer", ['ngRoute']).factory("Consumer", ['$http', function($http) {
    var urls = {
        'login': "/api-token-auth/",
        'register': "/api/users/",
        'songs': "/api/songs",
        'add_song': "/api/songs/",
        'playlist_user': "/api/playlist/user/{user}/",
        'add_playlist': "/api/playlist/",
        'public_playlists': "/api/playlist/public/"
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
        },
        'songs': function(token){
            return $http({
                method: 'GET',
                url: urls.songs,
                headers: {
                    'Authorization': "jwt "+token
                }
            });
        },
        'add_song': function(data, token){
            return $http({
                method: 'POST',
                data: data,
                url: urls.add_song,
                headers: {
                    'Content-Type': "application/json",
                    'Authorization': "jwt "+token
                }
            });
        },
        'get_playlist_users': function(id, token){
            return $http({
                method: 'GET',
                url: urls.playlist_user.replace("{user}", id),
                headers: {
                    'Authorization': "jwt "+token
                }
            });
        },
        add_playlist: function(data, token){
            return $http({
                method: 'POST',
                data: data,
                url: urls.add_playlist,
                headers: {
                    'Content-Type': "application/json",
                    'Authorization': "jwt "+token
                }
            });
        },
        get_public_playlists: function(){
             return $http({
                method: 'GET',
                url: urls.public_playlists,
                headers: {
                }
            });
        }
    }
}])
