angular.module('songsList').component('songDetail', {
    template: `
		<div class="panel panel-info song_info" >
			<div class="panel-heading">{{ $ctrl.data.id}} - {{ $ctrl.data.name}}</div>
			<div class="panel-body">
				<ul>
					<li>
						<strong>Artista</strong>
						<span>{{ $ctrl.data.artist}}</span>
					</li>
					<li>
						<strong>Album</strong>
						<span>{{ $ctrl.data.album}}</span>
					</li>
					<li>
						<strong>Duración</strong>
						<span>{{ $ctrl.data.duration}}</span>
					</li>
				</ul>
			</div>
		</div>
   `,
    bindings: {
        data: '='
    }
});
