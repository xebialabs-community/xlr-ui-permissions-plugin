angular
		.module('myRepo', [])
		.config(
				function($httpProvider) {

					// The following code retrieves credentials from the main XL Deploy application
					// and tells AngularJS to append them to every request.
					var flexApp = parent.document
							.getElementById("flexApplication");
					if (flexApp)
						$httpProvider.defaults.headers.common.Authorization = flexApp
								.getBasicAuth();

				})
		.controller(
				'RepoController',
				function($http, $scope) {
					$scope.globalperms= [ 'template#view','template#create_release', 'template#edit', 'template#edit_security' ];
					$scope.allperms = ['release#view', 'release#edit', 'release#edit_security', 'release#start', 'release#abort', 'release#edit_task', 'release#reassign_task'];
												
					$scope.loadCis = function() {
						$http
								.get('/api/extension/permissions')
								.then(
										function(response) {
											// response.data.entity is the serialized version of what Jython script puts into
											// response.entity in the script.
											$scope.resultCis = response.data.entity;
										});
					};

					$scope.loadCis();
				});
