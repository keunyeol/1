serial.redirect(
SerialPin.USB_TX,
SerialPin.USB_RX,
BaudRate.BaudRate9600
)
basic.forever(function () {
    if (serial.readString() == "1") {
        basic.showIcon(IconNames.Scissors)
    }
    if (serial.readString() == "2") {
        music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.UntilDone)
    }
    if (serial.readString() == "3") {
        basic.showIcon(IconNames.Ghost)
    }
})
