angular.module("Config", ['ngRoute']).value("Config", {
	pusher: {
		'API_KEY': "574fe9df791589ba8b69",
		'USER_CHANNEL': "mymusic_user_{user}",
		'EVENT_SONG_RATE': "rate_sound",
		'EVENT_PLAYLIST_RATE': "rate_playlist"
	}
});