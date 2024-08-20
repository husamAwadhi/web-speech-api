<script setup>
import axios from "axios"
import PrimaryButton from '../components/buttons/PrimaryButton.vue'
import SecondaryButton from '../components/buttons/SecondaryButton.vue'
import ScoreSummary from '../components/ScoreSummary.vue'
import TopBar from "../components/TopBar.vue"
import { default as ParagraphSkeleton } from '../components/skeletons/Paragraph.vue'
import { default as DangerToast } from '../components/toasts/Danger.vue'
</script>
<template>
    <TopBar />
    <div class="mx-auto max-w-screen-xl">
        <div class="max-w-7xl mx-5 lg:mx-20 lg:mt-14 lg:mb-5 mt-7 font-normal mb-24">
            <h2 :class="!showScore ? 'mb-5 lg:mb-8 text-base lg:text-2xl tracking-tight font-bold text-slate-900' :
                'mb-5 lg:mb-8 text-base lg:text-2xl tracking-tight font-bold text-slate-900 hidden lg:block'">
                Read the following paragraph as naturally and clearly as possible</h2>
            <div class="lg:grid lg:grid-flow-row lg:grid-cols-12">
                <div v-if="showScore" class="lg:col-span-12">
                    <ScoreSummary :scoreSummary="scoreSummary">
                        <div class="mt-8 mx-4 flex flex-row justify-center lg:col-span-8 lg:order-3">
                            <SecondaryButton text="Try Again" @click="resetScore" class="mr-4 lg:mr-14" />
                            <PrimaryButton text="Next Page" @click="nextParagraph" class="grow max-w-40 lg:max-w-64"
                                :disabled="isRecording || loading" v-show="hasNextParagraph" />
                        </div>
                    </ScoreSummary>
                </div>
                <p class="min-h-52 lg:min-h-72 font-normal leading-[26px] text-slate-700 text-base lg:text-lg lg:border lg:border-gray-200 lg:rounded-xl lg:shadow lg:p-6 lg:col-span-8"
                    v-else>
                    <ParagraphSkeleton v-if="loading" />
                    <template v-else>
                        {{ paragraph }}
                    </template>
                </p>
                <div class="fixed bottom-0 left-0 z-50 w-full h-20 bg-blue-50 lg:bg-white lg:relative lg:z-0 lg:h-fit lg:col-span-8"
                    v-if="!showScore">
                    <div class="m-5 flex flex-row justify-center">
                        <SecondaryButton text="Previous Page" @click="previousParagraph" v-show="hasPrevious"
                            class="mr-7 grow-0" :disabled="isRecording || loading" />
                        <PrimaryButton @click="toggleRecord" :disabled="loading" :text="recordingText()"
                            class="relative grow min-w-20 lg:max-w-64">
                            <div class="absolute top-1/2 -translate-y-1/2 left-[3px]">
                                <svg width="36" height="36" viewBox="0 0 36 36" fill="none"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <circle cx="18" cy="18" r="14" fill="white" />
                                    <path
                                        d="M2.71133 10.0113C1.66224 12.0191 1.01888 14.2138 0.817973 16.4701C0.61707 18.7265 0.86256 21.0004 1.54043 23.1619C2.2183 25.3234 3.31526 27.3302 4.7687 29.0678C6.22214 30.8053 8.00359 32.2396 10.0113 33.2887C12.0191 34.3378 14.2138 34.9811 16.4701 35.182C18.7265 35.3829 21.0004 35.1374 23.1619 34.4596C25.3234 33.7817 27.3302 32.6847 29.0678 31.2313C30.8053 29.7779 32.2396 27.9964 33.2887 25.9887C34.3378 23.9809 34.9811 21.7862 35.182 19.5298C35.3829 17.2735 35.1374 14.9996 34.4596 12.8381C33.7817 10.6766 32.6847 8.6698 31.2313 6.93224C29.7779 5.19468 27.9964 3.76041 25.9887 2.71132C23.9809 1.66224 21.7862 1.01888 19.5298 0.817973C17.2735 0.61707 14.9996 0.862561 12.8381 1.54043C10.6766 2.2183 8.6698 3.31527 6.93224 4.76871C5.19468 6.22215 3.76041 8.00359 2.71132 10.0113L2.71133 10.0113Z"
                                        :stroke="isRecording ? '#E11D48' : 'white'" stroke-width="1.5"
                                        stroke-linecap="round" stroke-linejoin="round" />
                                    <path
                                        d="M17.5687 9.875C18.3932 9.875 19.1839 10.2091 19.7669 10.8037C20.3499 11.3984 20.6774 12.2049 20.6774 13.0458V16.9708C20.6774 17.8118 20.3499 18.6183 19.7669 19.213C19.1839 19.8076 18.3932 20.1417 17.5687 20.1417C16.7443 20.1417 15.9536 19.8076 15.3706 19.213C14.7876 18.6183 14.4601 17.8118 14.4601 16.9708V13.0458C14.4601 12.2049 14.7876 11.3984 15.3706 10.8037C15.9536 10.2091 16.7443 9.875 17.5687 9.875ZM18.7697 21.8125V25.8583C18.7697 25.9283 18.7427 25.9955 18.6946 26.0454C18.6464 26.0953 18.581 26.1239 18.5124 26.125H16.6251C16.5565 26.1239 16.491 26.0953 16.4429 26.0454C16.3947 25.9955 16.3677 25.9283 16.3677 25.8583V21.8125"
                                        :fill="isRecording ? '' : '#1D4ED8'" />
                                    <path
                                        d="M18.7697 21.8125V25.8583C18.7697 25.9283 18.7427 25.9955 18.6946 26.0454C18.6464 26.0953 18.581 26.1239 18.5124 26.125H16.6251C16.5565 26.1239 16.491 26.0953 16.4429 26.0454C16.3947 25.9955 16.3677 25.9283 16.3677 25.8583V21.8125M17.5687 9.875C18.3932 9.875 19.1839 10.2091 19.7669 10.8037C20.3499 11.3984 20.6774 12.2049 20.6774 13.0458V16.9708C20.6774 17.8118 20.3499 18.6183 19.7669 19.213C19.1839 19.8076 18.3932 20.1417 17.5687 20.1417C16.7443 20.1417 15.9536 19.8076 15.3706 19.213C14.7876 18.6183 14.4601 17.8118 14.4601 16.9708V13.0458C14.4601 12.2049 14.7876 11.3984 15.3706 10.8037C15.9536 10.2091 16.7443 9.875 17.5687 9.875Z"
                                        stroke="white" stroke-width="0.421429" stroke-linecap="round"
                                        stroke-linejoin="round" />
                                    <path
                                        d="M12.7607 17.9121C12.9817 19.0469 13.5817 20.0684 14.4584 20.8025C15.3352 21.5366 16.4344 21.9379 17.5687 21.9379C18.703 21.9379 19.8022 21.5366 20.6789 20.8025C21.5556 20.0684 22.1557 19.0469 22.3767 17.9121"
                                        :stroke="isRecording ? 'white' : '#1D4ED8'" stroke-width="0.842857"
                                        stroke-linecap="round" stroke-linejoin="round" />
                                    <path d="M14.9134 26.125H20.4281" :stroke="isRecording ? 'white' : '#1D4ED8'"
                                        stroke-width="1.26429" stroke-linecap="round" />
                                    <rect id="Rectangle 3609" x="12" y="12" width="12" height="12" rx="2"
                                        :fill="isRecording ? '#E11D48' : ''" />
                                </svg>
                            </div>
                        </PrimaryButton>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <DangerToast :message="error.message" v-show="error.message.length > 0">
        <template #cta>
            <a class="text-sm font-medium text-blue-600 p-1.5 hover:bg-blue-100 rounded-lg cursor-pointer"
                @click="tryAgain">Try Again</a>
            <button type="button" @click="clearError"
                class="ms-auto -mx-1.5 -my-1.5 bg-white text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex items-center justify-center h-8 w-8">
                <span class="sr-only">Close</span>
                <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
                </svg>
            </button>
        </template>
    </DangerToast>
</template>
<script>
export default {
    data() {
        return {
            loading: true,
            showScore: false,
            hasNextParagraph: false,
            hasPrevious: false,
            isRecording: false,
            recognition: null,
            transcript: '',
            paragraph: '',
            scoreSummary: this.setScore(),
            error: { message: '', action: '' },
            recordStart: Date,
            paragraphId: Number,
            duration: Number,
        }
    },
    async mounted() {
        this.setupRecognition()
        this.getParagraph()
    },
    methods: {
        async getParagraph() {
            this.resetScore()
            this.clearError()
            this.loading = true
            this.paragraph = ''
            try {
                const response = await axios.post('/reading-task', { "id": this.paragraphId })
                this.paragraph = response.data.paragraph
                this.paragraphId = response.data.id
                this.hasNextParagraph = response.data.hasNext
                this.hasPrevious = response.data.hasPrevious
                this.loading = false
            } catch (err) {
                this.raiseError("paragraph")
            }
        },
        setScore(wpm = 0, fluency = 0, content = 0, pronunciation = 0, overall = 0, result = []) {
            return {
                wpm: wpm,
                fluency: fluency,
                content: content,
                pronunciation: pronunciation,
                overall: overall,
                result: result,
            }
        },
        nextParagraph() {
            this.paragraphId++
            this.getParagraph()
        },
        previousParagraph() {
            this.paragraphId--
            this.getParagraph()
        },
        setupRecognition() {
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
            this.recognition = new SpeechRecognition()
            this.recognition.continuous = true
            this.recognition.lang = "en-US"

            this.recognition.onstart = () => {
                this.isRecording = true
                this.recordStart = new Date()
            }

            this.recognition.onend = async () => {
                const endTime = new Date()
                this.duration = (endTime.getTime() - this.recordStart.getTime()) / 1000
                this.isRecording = false

                if (this.transcript.length > 0) {
                    this.submitTranscript()
                }
            }

            this.recognition.onresult = async (event) => {
                this.transcript = Array.from(event.results)
                    .map(result => result[0])
                    .map(result => result.transcript)
                    .join('')
            }
        },
        toggleRecord() {
            if (!this.isRecording) {
                this.resetScore()
                this.recognition.start()
            } else {
                this.recognition.stop()
            }
        },
        recordingText() {
            return (this.isRecording ? "Stop" : "Start") + " Recording"
        },
        resetScore() {
            this.showScore = false
            this.scoreSummary = this.setScore()
        },
        async submitTranscript() {
            this.loading = true
            this.clearError()
            try {
                const response = await axios.post(
                    '/score',
                    {
                        "id": this.paragraphId,
                        "transcript": this.transcript,
                        "duration": this.duration,
                    })
                this.scoreSummary = this.setScore(
                    parseFloat(response.data.wpm),
                    parseFloat(response.data.fluency),
                    parseFloat(response.data.content),
                    parseFloat(response.data.pronunciation),
                    parseFloat(response.data.overall),
                    response.data.result
                )
                this.transcript = ''
                this.showScore = true
                this.loading = false
            } catch (err) {
                this.raiseError("transcript")
            }
        },
        tryAgain() {
            switch (this.error.action) {
                case "transcript":
                    this.submitTranscript()
                    break;
                default:
                    this.getParagraph()
            }
        },
        clearError() {
            this.raiseError('', '')
        },
        raiseError(action, message = "Error while retrieving data.") {
            this.error = { message: message, action: action }
        }
    }
}
</script>
