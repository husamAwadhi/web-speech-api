<template>
    <dl>
        <dt class="font-semibold leading-[21px]">{{title}}</dt>
        <dd class="flex items-center mb-3">
            <div class="w-full bg-white rounded h-2.5 me-2">
                <div class="bg-blue-700 h-2.5 rounded" :style="{ 'width': percentage + '%' }">
                </div>
            </div>
            <span class="ml-3 font-semibold leading-[21px]">{{ score.toFixed(1) }}</span>
        </dd>
    </dl>
</template>
<script>
export default {
    props: {
        title: String,
        percentage: Number,
        score: Number,
    }
}
</script>
