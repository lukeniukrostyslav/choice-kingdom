package com.choicekingdom.app

import android.view.HapticFeedbackConstants
import android.view.SoundEffectConstants
import android.view.View
import androidx.compose.ui.hapticfeedback.HapticFeedback
import androidx.compose.ui.hapticfeedback.HapticFeedbackType

/**
 * Offline interaction feedback policy for Choice Kingdom.
 *
 * The controller deliberately uses platform feedback primitives: no network,
 * no external service and no mandatory audio assets. Premium authored audio
 * remains a later asset/content concern rather than being faked as complete.
 */
class ChoiceKingdomFeedback(
    private val haptics: HapticFeedback,
    private val view: View,
) {
    fun choicePressed() {
        haptics.performHapticFeedback(HapticFeedbackType.TextHandleMove)
        view.playSoundEffect(SoundEffectConstants.CLICK)
    }

    fun navigationChanged() {
        haptics.performHapticFeedback(HapticFeedbackType.TextHandleMove)
    }

    fun error() {
        view.performHapticFeedback(HapticFeedbackConstants.REJECT)
    }
}
