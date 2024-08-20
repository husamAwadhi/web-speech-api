<template>
    <button
        :class="disabled ?
            'items-center justify-center p-3 rounded-[20px] font-bold leading-[18px] gap-1 text-[13px] text-center text-white bg-primary-700 cursor-not-allowed' :
            'items-center justify-center p-3 rounded-[20px] font-bold leading-[18px] gap-1 text-[13px] text-center text-white bg-primary-700 hover:bg-primary-800'"
        :disabled="disabled">
        {{ text }}
        <slot />
    </button>
</template>
<script>
export default {
    props: {
        text: String,
        disabled: false
    }
}
</script>
