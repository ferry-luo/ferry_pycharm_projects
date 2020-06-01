angular.module('myApp', []).controller('userCtrl', function ($scope) {
    $scope.fName = '';
    $scope.lName = '';
    $scope.passw1 = '';
    $scope.passw2 = '';
    $scope.users = [
        {id:1,fName:'ferry',lName:'luo'},
        {id: 2, fName: 'Kim', lName: "Pim"},
        {id: 3, fName: 'Sal', lName: "Smith"},
        {id: 4, fName: 'Jack', lName: "Jones"},
        {id: 5, fName: 'John', lName: "Doe"},
        {id: 6, fName: 'Peter', lName: "Pan"}
    ];

    //默认edit为true，则在HTML，默认显示“创建新用户”
    $scope.edit = true;
    //默认error为false，表示两次密码一致
    $scope.error = false;
    //默认incomplete为false，表示姓名、两次密码都是完整的
    $scope.incomplete = false;

    //HTML中，表格中的“编辑”和下方的“创建新用户”用的同一个属性editUser
    $scope.editUser = function(user_id){
        //当操作“创建新用户”
        if(user_id == 'new'){
            $scope.edit = true;
            $scope.incomplete = true;
            $scope.fName = '';
            $scope.lName = '';
        }
        //当操作“编辑”
        else{
            $scope.edit = false;
            $scope.fName = $scope.users[user_id - 1].fName;
            $scope.lName = $scope.users[user_id - 1].lName;
        }
    };

    $scope.$watch('passw1', function () {
        $scope.test();
    });
    $scope.$watch('passw2', function () {
        $scope.test();
    });
    $scope.$watch('fName', function () {
        $scope.test();
    });
    $scope.$watch('lName', function () {
        $scope.test();
    });

    $scope.test = function () {
        //创建新用户时，名字、姓氏、密码1、密码2，只要有空的，令incomplete为true
        if($scope.edit && (!$scope.fName.length || !$scope.lName.length || !$scope.passw1.length || !$scope.passw2.length)){
            $scope.incomplete = true;
        }
        else{
            //如果两次密码不一致，令error为true
            if($scope.passw1 != $scope.passw2){
                $scope.error = true;
            }
            else{
                $scope.error = false;
            }
        }
    }

});