app.controller("myNoteCtrl", function ($scope) {
    $scope.message = "";
    $scope.left = function () {
        return 100 - $scope.message.length;
    };
    $scope.clear = function () {
        $scope.message = "";
    };
    $scope.save = function () {
        alert('笔记已保存');
    }
});