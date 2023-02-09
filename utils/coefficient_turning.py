from db_access import CoefficientTurningDb


class CoefficientTurning:
    def __init__(self, init_guess) -> None:
        self.init_guess = init_guess
        pass

    def optimizer(self, task_uuid, coefficient_need_to_improve, optimizer_func) -> any:
        task_feature = self.get_task_feature(task_uuid)
        self.record(task_feature, coefficient_need_to_improve)
        new_coefficient = self.get_new_coefficient(task_feature, optimizer_func)
        return new_coefficient

    def get_task_feature(self, task_uuid) -> None:
        pass

    def record(self) -> None:
        pass

    def get_new_coefficient(self, task_feature, optimizer_func: function) -> any:
        pass


class TimeCoefficientTurning(CoefficientTurning):
    def __init__(
        self,
    ) -> None:
        super().__init__(self)
