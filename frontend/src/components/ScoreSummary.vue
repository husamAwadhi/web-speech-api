<script setup>
import Indicator from './Indicator.vue';
import Progress from './Progress.vue'
</script>
<template>
    <div class="lg:grid lg:grid-flow-row lg:grid-cols-12 lg:gap-3">
        <div class="bg-gray-100 p-5 rounded-lg text-slate-900 lg:order-2 lg:col-span-4 lg:shadow">
            <div class="flex items-center mb-5">
                <p class="inline-flex items-center font-semibold leading-[21px]">
                    Your Score: <span class="text-lg font-bold pl-3 text-blue-700">{{ scoreSummary.overall }}</span><span
                        class="text-lg pl-1">/ 5</span></p>
            </div>
            <div class="gap-[25px] grid grid-cols-1">
                <Progress title="Content" :score="scoreSummary.content" :percentage="(scoreSummary.content / 5) * 100" />
                <Progress title="Fluency" :score="scoreSummary.fluency" :percentage="(scoreSummary.fluency / 5) * 100" />
                <Progress title="Pronunciation" :score="scoreSummary.pronunciation"
                    :percentage="(scoreSummary.pronunciation / 5) * 100" />
            </div>
        </div>
        <hr class="my-5 h-px border-t-0 bg-gray-200 lg:hidden" />
        <div
            class="lg:col-span-8 min-h-52 lg:min-h-72 font-normal leading-[26px] text-slate-700 text-base lg:text-lg lg:border lg:border-gray-200 lg:rounded-xl lg:shadow lg:p-6 lg:order-1">
            <div class="inline-flex py-2 gap-5">
                <Indicator text="Match" color="green" />
                <Indicator text="Partial Match" color="yellow" />
                <Indicator text="Mismatch" color="red" />
            </div>
            <p class="mt-6">
                <template v-for="item in scoreSummary.result">
                    <span v-if="item.type == 'match'"
                        class="font-medium inline-flex items-center bg-green-100 text-green-800 pr-1">{{
                            item.word }}</span>
                    <span v-else-if="item.type == 'partial'"
                        class="font-medium inline-block pr-1 bg-yellow-100 text-yellow-800">
                        {{ item.word }}</span>
                    <span v-else class="font-medium inline-block pr-1 bg-red-100 text-red-800">{{ item.word }}</span>
                </template>
            </p>
        </div>
        <slot />
    </div>
</template>
<script>
export default {
    props: {
        scoreSummary: Object
    }
}
</script>
