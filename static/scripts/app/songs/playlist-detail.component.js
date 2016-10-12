angular.module('songsList').component('playlistDetail', {
    template: `
		<div class="panel panel-primary playlist_info" >
			<div class="panel-heading">{{ $ctrl.data.id}} - {{ $ctrl.data.name}}</div>
			<div class="panel-body">
				<ul>
					<li>
						<strong>Genero</strong>
						<span>{{ $ctrl.data.gender}}</span>
					</li>
					<li>
						<strong>Descripción</strong>
						<span>{{ $ctrl.data.description}}</span>
					</li>
				</ul>
			</div>
		</div>
   `,
    bindings: {
        data: '='
    }
});
