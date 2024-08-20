<template>
    <!-- class="bg-yellow-100 bg-red-100 bg-green-100" -->
    <span
        class="inline-flex items-center w-fit whitespace-nowrap text-slate-900 text-sm">
        <span :class="`w-6 h-6 me-1 bg-${color}-100 rounded-full`"></span>
        {{ text }}
    </span>
</template>
<script>
export default {
    props: {
        color: String,
        text: String,
    }
}
</script>
