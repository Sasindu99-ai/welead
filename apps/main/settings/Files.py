from vvecon.zorion import utils

__all__ = ["Files"]


class Files(utils.Files):
    common = utils.FileMaker(
        bootstrap="bootstrap.min",
        style="style",
    )

    css = utils.FileMaker(
        colors="colors",
        all="all.min",
        animate="animate.min",
    )

    js = utils.FileMaker(
        # JS
        serviceWorker="service-worker",
        bootstrap=("bootstrap/bootstrap", 1, "util"),
        bootstrapBundle=("bootstrap/bootstrap.bundle.min", 1, "util"),
        popper=("bootstrap/popper", 1, "util"),
        jQuery=("jquery/jquery.min", 1, "util"),
        slim=("jquery/slim", 1, "util"),
        main="main",
        models="models",
        api="api",
        loader="Loader",
        util=("util", 1, "util"),
        # Plugins
        moment=("ui/moment/moment.min", 1, "util/vendor"),
        datePicker=("pickers/datepicker.min", 1, "util/vendor"),
        dateRangePicker=("pickers/daterangepicker", 1, "util/vendor"),
        steps=("forms/wizards/steps.min", 1, "util/vendor"),
        validation=("forms/validation/validate.min", 1, "util/vendor"),
        autoComplete=("forms/inputs/autocomplete.min", 1, "util/vendor"),
        select2=("forms/selects/select2.min", 1, "util/vendor"),
        sweetAlert=("notifications/sweet_alert.min", 1, "util/vendor"),
        cryptojs=("extensions/cryptojs", 1, "util/vendor"),
        noUiSlider=("sliders/nouislider.min", 1, "util/vendor"),
        swiper=("sliders/swiper/swiper-bundle.min", 1, "util/vendor"),
    )

    font = utils.FileMaker(
        poppins="poppins/poppins",
    )

    icon = utils.FileMaker(
        phosphor="phosphor/styles.min",
        icomoon="icomoon/styles.min",
        bootstrap="bootstrap/bootstrap-icons.min",
    )
