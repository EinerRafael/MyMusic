angular.module('Home').component('songDetail2', {
    template: `
		<div class="panel panel-info">
			<div class="panel-heading">{{ $ctrl.data.name}}</div>
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
				</ul>
			</div>
		</div>
   `,
    bindings: {
    	data: "="
    }, 
    controller: ['Consumer', function (Consumer) {
    }]
});
